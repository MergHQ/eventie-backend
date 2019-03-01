
exports.up = function(knex, Promise) {
  return knex.schema.hasTable('events').then(function(exists) {
    if (exists) {
      return knex.schema.raw('ALTER TABLE events ADD COLUMN author_id VARCHAR(255) REFERENCES users(id);')
    }
  })
}

exports.down = function(knex, Promise) {
  
};


exports.up = function(knex, Promise) {
  return knex.schema.hasTable('events').then(function(exists) {
    if (!exists) {
      return knex.schema.createTable('events', function(table) {
        table.string('id').primary()
        table.string('name')
        table.string('description')
        table.date('registration_start')
        table.date('registration_end')
        table.date('time')
        table.integer('max_participants')
      });
    }
  });
  
};

exports.down = function(knex, Promise) {
  return knex.schema.hasTable('events')
    .then(exists => {
      if (exists) {
        knex.schema.dropTable('events')
      }
    })
};

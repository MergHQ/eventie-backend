
exports.up = function(knex, Promise) {
  return knex.schema.hasTable('users').then(function(exists) {
    if (!exists) {
      return knex.schema.createTable('users', function(table) {
        table.string('id').primary()
        table.string('username')
        table.string('email')
        table.string('name')
        table.string('password_salt')
      });
    }
  });
  
};

exports.down = function(knex, Promise) {
  return knex.schema.hasTable('users')
  .then(exists => {
    if (exists) {
      knex.schema.dropTable('users')
    }
  })
};

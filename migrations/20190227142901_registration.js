
exports.up = function(knex, Promise) {
  return knex.schema.hasTable('registrations').then(function(exists) {
    if (!exists) {
      return knex.schema.createTable('registrations', function(table) {
        table.string('user_id').references('users.id')
        table.string('event_id').references('events.id')
      });
    }
  });
};

exports.down = function(knex, Promise) {
  return knex.schema.hasTable('registrations')
  .then(exists => {
    if (exists) {
      knex.schema.dropTable('registrations')
    }
  })
};

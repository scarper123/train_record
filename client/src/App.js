import React from 'react';
import
{
  Admin,
  Resource,
  ListGuesser,
  EditGuesser
}
from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';
// import simpleRestProvider from 'ra-data-simple-rest'
import PostIcon from '@material-ui/icons/Book';
import UserIcon from '@material-ui/icons/Group';

import Dashboard from './Dashboard';
import authProvider from './authProvider';
import dataProvider from './dataProvider';
import {UserList, UserCreate, UserEdit } from './users';
import { RecordList, RecordEdit, RecordCreate } from './records';

const App = () => (
  <Admin dashboard={Dashboard} authProvider={authProvider} dataProvider={dataProvider}>
    <Resource name="records" list={RecordList} edit={RecordEdit} create={RecordCreate} icon={PostIcon} />
    <Resource name="courses" list={ListGuesser} edit={EditGuesser} />
    <Resource name="users" list={UserList} edit={UserEdit} create={UserCreate} icon={UserIcon} />
    <Resource name="roles" list={ListGuesser} edit={EditGuesser} />
  </Admin>
);

export default App;
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


import authProvider from './providers/authProvider';
import dataProvider from './providers/dataProvider';
import Dashboard from './components/Dashboard';
import {UserList, UserCreate, UserEdit } from './components/users';
import { RecordList, RecordEdit, RecordCreate } from './components/records';
import { CourseList, CourseEdit, CourseCreate } from './components/courses';
import { RoleList, RoleEdit, RoleCreate } from './components/roles';

const App = () => (
  <Admin dashboard={Dashboard} authProvider={authProvider} dataProvider={dataProvider}>
    <Resource name="records" list={RecordList} edit={RecordEdit} create={RecordCreate} icon={PostIcon} />
    <Resource name="courses" list={CourseList} edit={CourseEdit} create={CourseCreate}/>
    <Resource name="users" list={UserList} edit={UserEdit} create={UserCreate} icon={UserIcon} />
    <Resource name="roles" list={RoleList} edit={RoleEdit} create={RoleCreate} />
  </Admin>
);

export default App;
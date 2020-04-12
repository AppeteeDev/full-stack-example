import { Component, OnInit } from '@angular/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { MatInputModule } from '@angular/material/input';
import { FormsModule, FormBuilder, FormGroup } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';

import { ThemeService, Theme } from '../../../DebatIDOAPI';

@Component({
  selector: 'app-theme-form-new',
  templateUrl: './theme-form-new.component.html',
  styleUrls: ['./theme-form-new.component.scss']
})

export class ThemeFormNewComponent implements OnInit {

  themeFormGroup: FormGroup;

  constructor(private _formBuilder: FormBuilder, private themeService: ThemeService) {}

  ngOnInit() {
      this.formBuild();
  }

  formBuild(){
    this.themeFormGroup = this._formBuilder.group({
      title:['']
    });
  }

  onSubmitForm() {
    let myNewTheme = {} as Theme;
    myNewTheme.title = this.themeFormGroup.value.title
    this.themeService.themePost(myNewTheme).subscribe();
  }

}
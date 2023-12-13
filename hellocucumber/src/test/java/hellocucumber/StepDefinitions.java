package hellocucumber;

import io.cucumber.java.en.*;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Assertions.*;

public class StepDefinitions {

    
  IsItFriday isItFriday = new IsItFriday();

    @Given("an example scenario")
    public void anExampleScenario() {
    }

    @When("all step definitions are implemented")
    public void allStepDefinitionsAreImplemented() {
    }

    @Then("the scenario passes")
    public void theScenarioPasses() {
    }

    
    

    @Given("today is Sunday")
    public void today_is_sunday() {
        isItFriday.setToday("Sunday");
    }

    @Given("today is Friday")
    public void today_is_friday() {
        isItFriday.setToday("Friday");
    }

     @Given("today is {string}")
    public void today_is_friday(String string) {
        isItFriday.setToday(string);
    }

    @When("I ask whether it's Friday yet")
    public String i_ask_whether_it_s_friday_yet() {

        if(isItFriday.getToday().equals("Friday")){
            return "TGIF";
        }else{
            return "Nope";
        }
    }
    @Then("I should be told {string}")
    public void i_should_be_told(String string) {
        Assertions.assertEquals(i_ask_whether_it_s_friday_yet(), string);
    }

}

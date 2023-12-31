import { NextPage } from "next";
import { useState } from "react";
import { useRouter } from "next/router";
import { useMutation, useQueryClient } from "react-query";

import Container from "@/components/layout/Container";
import Card from "@/components/ui/Card";
import Button from "@/components/ui/Button";
import OnBoardingUserDetail from "@/components/ui/onBoarding/OnBoardingUserDetailForm";
import OnBoardingOrganizationDetailForm from "@/components/ui/onBoarding/OnBoardingOrganizationDetailForm";
import Alert from "@/components/ui/Alert";

import { UpdateUser } from "@/models/users";
import userService from "@/services/auth/UserService";
import { useAuth } from "@/hooks/auth/useAuth";
import useCurrentUser from "@/hooks/users/useCurrentUser";

import { GrPrevious, GrNext } from "react-icons/gr";

const OnBoardingPage: NextPage = () => {
  const { isAuthenticated } = useAuth();
  const { data: currentUser, isLoading, isError } = useCurrentUser();
  const [step, setStep] = useState<number>(1);
  const [errMsg, setErrMsg] = useState<string | null>(null);
  const router = useRouter();

  const steps = ["welcome", "name", "tenant name", "completion"];

  const queryClient = useQueryClient();

  const mutation = useMutation(
    async (data: UpdateUser) => await userService.updateCurrentUser(data)
  );

  const onSubmit = async () => {
    if (step < steps.length) {
      setStep(step + 1);
    } else {
      const data = {
        is_onboarded: true,
      };
      try {
        await mutation.mutateAsync(data);
        queryClient.invalidateQueries("currentUser");
        router.push("/projects");
      } catch (error: any) {
        setErrMsg(error);
      }
    }
  };

  return (
    <>
      {errMsg && <Alert message={errMsg} severity="error" />}
      <Container centered>
        <Card transparent fixedSize="w-1/4">
          {step === 1 && (
            <>
              <h1 className="text-4xl font-bold mb-4">Welcome to Devjutsu</h1>
              <p>
                Embark on your coding journey with the spirit of a samurai.
                Before you dive in, let's set up your dojo by capturing some
                essential details. Your path to mastering the art of code begins
                here.
              </p>
            </>
          )}
          {step === 2 && <OnBoardingUserDetail onNextStep={onSubmit} />}
          {step === 3 && (
            <OnBoardingOrganizationDetailForm
              onNextStep={onSubmit}
              currentUserId={currentUser?.id}
            />
          )}
          {step === 4 && (
            <>
              <h1 className="text-4xl font-bold mb-4">You're all set</h1>
              <p>
                Thank you for setting up your profile. You're now ready to
                embark on your Devjutsu journey. Dive in and start exploring!
              </p>
              <Button text="Finish" type="submit" onClick={onSubmit} bgFrost />
            </>
          )}
        </Card>
        {/* BEGIN Prev & Next Buttons */}
        <div className="fixed left-4 top-1/2 transform -translate-y-1/2">
          {step > 1 && (
            <Button
              icon={<GrPrevious size={25} />}
              onClick={() => setStep(step - 1)}
              polarNightMedium
              rounded="rounded-full"
            />
          )}
        </div>
        {step == 1 && (
          <div className="fixed right-4 top-1/2 transform -translate-y-1/2">
            <Button
              icon={<GrNext size={25} />}
              polarNightMedium
              onClick={onSubmit}
              rounded="rounded-full"
              type="button"
            />
          </div>
        )}
        {/* END Prev & Next Buttons */}
      </Container>
    </>
  );
};

export default OnBoardingPage;

import { NextPage } from "next";
import { useForm } from "react-hook-form";
import { useMutation } from "react-query";
import { yupResolver } from "@hookform/resolvers/yup";
import { useRouter } from "next/router";
import Cookies from "js-cookie";

import authService from "@/services/auth";
import { signUpSchema } from "@/utils/validationSchemas/auth";

import Container from "@/components/layout/Container";
import Button from "@/components/ui/Button";
import Card from "@/components/ui/Card";
import FormGroup from "@/components/forms/FormGroup";
import CustomInput from "@/components/forms/CustomInput";
import OAuth from "@/components/auth/OAuth";

import { AiFillMail } from "react-icons/ai";

interface SignUpFormData {
  email: string;
  password: string;
  confirmPassword: string;
}

const SignUpPage: NextPage = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<SignUpFormData>({
    resolver: yupResolver(signUpSchema),
    mode: "onChange",
  });
  const router = useRouter();

  const mutation = useMutation(({ email, password }) =>
    authService.signUp(email, password)
  );

  const onSubmit = (data: SignUpFormData) => {
    mutation.mutate(data, {
      onSuccess: () => {
        authService.requestVerifyToken(data.email);
        Cookies.set("userRegistered", "true", { expires: 1 });
        Cookies.set("registeredEmail", data.email, { expires: 1 });
        router.push("/signup/success");
      },
      onError: (error: Error) => {
        console.log(error.message);
      },
    });
  };

  return (
    <Container centered>
      <Card transparent fixedSize="w-1/4">
        <h1 className="text-5xl font-extrabold text-nord-snowstorm-light mb-6 text-center">
          Sign Up
        </h1>
        <form onSubmit={handleSubmit(onSubmit)}>
          <FormGroup label="Work email">
            <CustomInput
              placeholder="Enter your email address ..."
              name="email"
              type="email"
              register={register}
              error={errors.email?.message}
            />
          </FormGroup>
          <FormGroup label="Password">
            <CustomInput
              placeholder="password ..."
              name="password"
              type="password"
              register={register}
              error={errors.password?.message}
            />
          </FormGroup>
          <FormGroup label="Confirm password">
            <CustomInput
              placeholder="confirm password ..."
              name="confirmPassword"
              type="password"
              register={register}
              error={errors.confirmPassword?.message}
            />
          </FormGroup>
          <Button
            icon={<AiFillMail />}
            type="submit"
            text="Continue with email"
            fullWidth
            bgFrost
          />
        </form>

        {mutation.isError ? (
          <div className="mt-4 text-nord-aurora-red">
            Error: {mutation.error?.message}
          </div>
        ) : null}

        <hr className="my-6 border-t border-nord-polar-night-medium" />

        <OAuth />

        <p
          className="text-center underline mt-6 cursor-pointer"
          onClick={() => router.push("/login")}
        >
          Already an account? Login here
        </p>
      </Card>
    </Container>
  );
};

export default SignUpPage;

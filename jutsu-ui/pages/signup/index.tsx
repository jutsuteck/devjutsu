import { NextPage } from "next";
import { useForm } from "react-hook-form";
import { useMutation } from "react-query";
import { yupResolver } from "@hookform/resolvers/yup";
import { useRouter } from "next/router";
import { AiFillGithub, AiFillGoogleCircle, AiFillMail } from "react-icons/ai";
import Cookies from "js-cookie";
import * as yup from "yup";

import authService from "@/services/auth";
import CenteredContainer from "@/components/layout/CenteredContainer";
import Button from "@/components/ui/Button";
import Card from "@/components/ui/Card";
import FormGroup from "@/components/forms/FormGroup";
import CustomInput from "@/components/forms/CustomInput";

interface SignUpFormData {
  email: string;
  password: string;
  confirmPassword: string;
}

const schema = yup.object().shape({
  email: yup
    .string()
    .required("Email is required")
    .email("Invalid email format"),
  password: yup
    .string()
    .required("Password is required")
    .min(12, "Password should be at least 12 characters")
    .matches(/^\S*$/, "Password should not contain any spaces"),
  confirmPassword: yup
    .string()
    .oneOf([yup.ref("password"), null], "Passwords must match"),
});

const SignUpPage: NextPage = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<SignUpFormData>({
    resolver: yupResolver(schema),
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
    <CenteredContainer>
      <Card transparent>
        <h1 className="text-5xl text-nord-snowstorm-light mb-6 text-center">
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
          />
        </form>

        {mutation.isError ? (
          <div className="mt-4 text-nord-aurora-red">
            Error: {mutation.error?.message}
          </div>
        ) : null}

        <hr className="my-6 border-t border-nord-polar-night-light" />

        <Button
          icon={<AiFillGithub />}
          text="Continue with Github"
          transparent
        />
        <Button
          icon={<AiFillGoogleCircle />}
          text="Continue with Google"
          className="mt-2"
          transparent
        />

        <p className="text-center underline mt-6">
          Already an account? Login here
        </p>
      </Card>
    </CenteredContainer>
  );
};

export default SignUpPage;

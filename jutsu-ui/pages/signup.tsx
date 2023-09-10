import { signUp } from "@/api/auth";
import { NextPage } from "next";
import { useForm } from "react-hook-form";
import { useMutation } from "react-query";

import * as yup from "yup";

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
  } = useForm<SignUpFormData>();

  const mutation = useMutation(signUp);

  const onSubmit = (data: SignUpFormData) => {
    mutation.mutate(data, {
      onSuccess: () => {
        console.log("Registration successfull");
      },
      onError: (error: Error) => {
        console.log(error.message);
      },
    });
  };

  return (
    <>
      <h1>Sign Up</h1>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div>
          <label>Email</label>
          <input type="email" {...register("email")} />
          {errors.email && <p>{errors.email.message}</p>}
        </div>
        <div>
          <label>Password</label>
          <input type="password" {...register("password")} />
          {errors.password && <p>{errors.password.message}</p>}
        </div>
        <div>
          <label>Confirm password</label>
          <input type="password" {...register("confirmPassword")} />
          {errors.password && <p>{errors.confirmPassword.message}</p>}
        </div>
        <button type="submit">Sign Up</button>
      </form>

      {mutation.isError ? <div>Error: {mutation.error?.message}</div> : null}
    </>
  );
};

export default SignUpPage;

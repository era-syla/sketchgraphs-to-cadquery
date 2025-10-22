import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.17614, -0.3578).lineTo(0.14807, -0.27354).lineTo(0.21976, -0.26606).threePointArc((0.25166, -0.25283), (0.27115, -0.22433)).lineTo(0.30739, -0.2361).threePointArc((0.3131, -0.23403), (0.31913, -0.23472)).lineTo(0.37396, -0.25195).threePointArc((0.29863, -0.34896), (0.17614, -0.3578)).close()
solid=wp_sketch0.add(loop0).extrude(0.4990427396003283)

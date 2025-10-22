import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05462, 0.0).lineTo(-0.0, 0.02283).lineTo(0.0, 0.18482).lineTo(0.01037, 0.24362).lineTo(0.02451, 0.24362).lineTo(0.02451, 0.02391).lineTo(0.06062, -0.0).lineTo(-0.05462, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.5120122246700552)

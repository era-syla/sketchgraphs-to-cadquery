import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02942, -0.0).lineTo(-0.03, 0.01875).lineTo(-0.03, 0.03125).lineTo(-0.02942, 0.05).lineTo(-0.0266, 0.05).lineTo(-0.0266, 0.0).lineTo(-0.02942, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.14899615898107613)

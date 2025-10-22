import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-2.8194, -0.68468).lineTo(-2.667, -0.68468).lineTo(-2.667, -0.07508).lineTo(-2.8194, -0.07508).lineTo(-2.8194, -0.68468).close()
solid=wp_sketch0.add(loop0).extrude(1.0888122740419564)

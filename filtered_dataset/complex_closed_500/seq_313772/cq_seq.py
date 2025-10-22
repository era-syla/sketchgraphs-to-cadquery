import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-1.04, -0.04).lineTo(-2.04, -0.04).lineTo(-2.04, -0.025).lineTo(-1.055, -0.025).lineTo(-1.04, -0.04).close()
solid=wp_sketch0.add(loop0).extrude(-0.5194793269805613)

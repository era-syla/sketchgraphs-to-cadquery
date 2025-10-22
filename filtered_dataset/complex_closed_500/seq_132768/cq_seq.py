import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04354, -0.03319).lineTo(-0.026, -0.03319).lineTo(-0.026, -0.02057).lineTo(-0.04354, -0.02057).lineTo(-0.04354, -0.03319).close()
solid=wp_sketch0.add(loop0).extrude(0.029961291569670496)

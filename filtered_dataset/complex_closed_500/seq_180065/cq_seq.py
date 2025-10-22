import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.025, -0.07881).lineTo(-0.025, -0.09581).lineTo(-0.042, -0.09581).lineTo(-0.025, -0.07881).close()
solid=wp_sketch0.add(loop0).extrude(-0.034668904731532)

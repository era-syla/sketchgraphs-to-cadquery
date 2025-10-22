import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00615, -0.0014).lineTo(-0.00285, -0.0014).lineTo(-0.00285, 0.0014).lineTo(-0.00615, 0.0014).lineTo(-0.00615, -0.0014).close()
solid=wp_sketch0.add(loop0).extrude(-0.005243952279988381)

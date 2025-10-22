import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.005, -0.0175).lineTo(-0.005, -0.0175).lineTo(-0.005, -0.0325).lineTo(0.005, -0.0325).lineTo(0.005, -0.0175).close()
solid=wp_sketch0.add(loop0).extrude(0.035508330895027425)

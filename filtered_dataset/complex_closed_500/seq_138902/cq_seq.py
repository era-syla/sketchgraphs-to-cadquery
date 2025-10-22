import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.18155, 0.14897).lineTo(0.18155, 0.14897).lineTo(0.18155, -0.1524).lineTo(-0.18155, -0.1524).lineTo(-0.18155, 0.14897).close()
solid=wp_sketch0.add(loop0).extrude(0.8925007495611597)

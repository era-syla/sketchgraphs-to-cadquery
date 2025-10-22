import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.1016, 0.1524).lineTo(-0.1016, 0.1524).lineTo(-0.1016, -0.1524).lineTo(0.1016, -0.1524).lineTo(0.1016, 0.1524).close()
solid=wp_sketch0.add(loop0).extrude(0.8914400720881525)

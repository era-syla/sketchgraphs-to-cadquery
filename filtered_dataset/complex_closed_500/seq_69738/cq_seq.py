import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05, 0.55).lineTo(-1.0, 0.925).lineTo(-1.33, 0.925).lineTo(-1.33, 0.55).lineTo(-0.05, 0.55).close()
solid=wp_sketch0.add(loop0).extrude(1.1680782106621133)

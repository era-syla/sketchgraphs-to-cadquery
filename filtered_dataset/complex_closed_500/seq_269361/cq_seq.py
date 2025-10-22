import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.00483, 0.0).lineTo(0.00483, 0.00156).lineTo(0.00305, 0.00208).lineTo(0.0, 0.00208).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.000179474912861268)

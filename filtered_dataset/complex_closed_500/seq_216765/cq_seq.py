import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(2.4384, 0.0).lineTo(2.4384, 1.2192).lineTo(-0.0, 1.2192).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(4.447976306696532)

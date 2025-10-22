import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(1.066, 0.0).lineTo(1.066, 0.55).lineTo(-0.0, 0.55).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.3784651302464059)

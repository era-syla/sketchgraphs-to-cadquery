import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(1.9939, 0.0127).lineTo(2.20981, 0.22861).lineTo(2.20981, 0.0127).lineTo(1.9939, 0.0127).close()
solid=wp_sketch0.add(loop0).extrude(0.31453490419741353)

import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0425, 0.15203).lineTo(-0.0425, 0.15303).lineTo(0.0425, 0.11903).lineTo(0.0425, 0.11803).lineTo(-0.0425, 0.15203).close()
solid=wp_sketch0.add(loop0).extrude(0.09123820766987709)

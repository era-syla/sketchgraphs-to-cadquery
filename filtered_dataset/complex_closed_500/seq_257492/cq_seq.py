import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.29959, 0.0).lineTo(0.29959, 0.2345).lineTo(0.0, 0.2345).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.414701761178669)

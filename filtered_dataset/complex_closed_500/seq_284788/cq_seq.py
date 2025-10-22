import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.3048, 0.0).lineTo(0.3048, 2.032).lineTo(-0.0, 2.032).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(2.0324386563532917)

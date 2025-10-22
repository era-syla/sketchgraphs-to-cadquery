import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00167, 0.0).lineTo(0.00767, 0.0).lineTo(0.00767, 0.02).lineTo(0.00167, 0.02).lineTo(0.00167, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.032495199179192295)

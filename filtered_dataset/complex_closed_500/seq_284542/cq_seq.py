import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00916, 0.0118).lineTo(0.00984, 0.0118).lineTo(0.00893, 0.0088).lineTo(-0.00483, 0.00881).lineTo(-0.00916, 0.0118).close()
solid=wp_sketch0.add(loop0).extrude(0.0018860539029962266)

import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.30493, 0.0).lineTo(-0.31763, 0.0).lineTo(-0.31763, 0.1524).lineTo(-0.30493, 0.1524).lineTo(-0.30493, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.3272013219364491)

import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.20116, 0.0).lineTo(0.14973, 0.21925).lineTo(-0.05142, 0.21925).lineTo(0.0, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.18349909020596106)

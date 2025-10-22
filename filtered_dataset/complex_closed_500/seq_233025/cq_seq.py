import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, -0.346).lineTo(0.13026, 0.14012).lineTo(0.42597, 0.14012).lineTo(0.42597, -0.51026).lineTo(-0.42974, -0.51026).lineTo(-0.42974, 0.14012).lineTo(-0.13026, 0.14012).lineTo(0.0, -0.346).close()
solid=wp_sketch0.add(loop0).extrude(-1.125440920458687)

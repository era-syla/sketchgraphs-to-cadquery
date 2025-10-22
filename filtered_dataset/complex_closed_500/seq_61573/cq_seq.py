import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.1205, 0.1955).lineTo(0.1205, 0.1955).lineTo(0.1205, -0.1955).lineTo(-0.1205, -0.1955).lineTo(-0.1205, 0.1955).close()
solid=wp_sketch0.add(loop0).extrude(-1.0643254487291205)

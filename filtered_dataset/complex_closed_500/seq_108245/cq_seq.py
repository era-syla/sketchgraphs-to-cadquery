import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0875, 0.0875).lineTo(0.0875, 0.0875).lineTo(0.0875, -0.0875).lineTo(-0.0875, -0.0875).lineTo(-0.0875, 0.0875).close()
solid=wp_sketch0.add(loop0).extrude(0.2571782738667252)

import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(6.075, -5.875).lineTo(13.775, -5.875).lineTo(13.775, 6.625).lineTo(-13.925, 6.625).lineTo(-13.925, -1.375).lineTo(-5.925, -1.375).lineTo(-5.925, 0.625).lineTo(6.075, 0.625).lineTo(6.075, -5.875).close()
solid=wp_sketch0.add(loop0).extrude(5.532292384939914)

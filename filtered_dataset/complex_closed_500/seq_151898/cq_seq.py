import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.508, 6.096).lineTo(0.4064, 6.096).lineTo(0.4064, 0.0).lineTo(0.508, 0.0).lineTo(0.508, 6.096).close()
solid=wp_sketch0.add(loop0).extrude(-0.5382368772281568)

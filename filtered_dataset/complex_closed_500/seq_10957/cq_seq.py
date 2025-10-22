import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.23482, 0.26495).lineTo(0.04458, 0.26495).lineTo(0.04458, -0.01445).lineTo(-0.23482, -0.01445).lineTo(-0.23482, 0.26495).close()
solid=wp_sketch0.add(loop0).extrude(0.4872863253264091)

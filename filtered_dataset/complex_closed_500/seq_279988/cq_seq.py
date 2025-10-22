import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01019, -0.00956).lineTo(0.00981, -0.00956).lineTo(0.00981, 0.01044).lineTo(-0.01019, 0.01044).lineTo(-0.01019, -0.00956).close()
solid=wp_sketch0.add(loop0).extrude(0.03448963412589318)

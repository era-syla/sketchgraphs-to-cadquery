import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00546, 0.01624).lineTo(-0.00546, 0.01624).lineTo(-0.00546, 0.03225).threePointArc((-0.00565, 0.03443), (-0.00621, 0.03654)).lineTo(0.00621, 0.03654).threePointArc((0.00565, 0.03443), (0.00546, 0.03225)).lineTo(0.00546, 0.01624).close()
solid=wp_sketch0.add(loop0).extrude(-0.04423570498846301)

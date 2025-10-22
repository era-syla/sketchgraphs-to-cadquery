import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.08944, 0.05352).lineTo(0.10144, 0.05352).lineTo(0.10144, 0.04056).lineTo(0.08944, 0.04056).lineTo(0.08944, 0.05352).close()
solid=wp_sketch0.add(loop0).extrude(0.024847009135048788)

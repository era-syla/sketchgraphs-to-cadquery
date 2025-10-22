import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.11, -0.035).lineTo(0.07, -0.035).lineTo(0.07, -0.065).lineTo(0.11, -0.065).lineTo(0.11, -0.035).close()
solid=wp_sketch0.add(loop0).extrude(-0.03949455166106353)

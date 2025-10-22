import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.27332, 0.0).lineTo(0.25427, 0.0).lineTo(0.25427, 0.91122).lineTo(0.27332, 0.91122).lineTo(0.27332, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.009330679431879324)

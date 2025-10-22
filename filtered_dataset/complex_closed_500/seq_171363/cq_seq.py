import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02075, 0.02895).lineTo(0.03932, 0.02895).lineTo(0.03932, -0.03577).lineTo(-0.02075, -0.03577).lineTo(-0.02075, 0.02895).close()
solid=wp_sketch0.add(loop0).extrude(-0.06256907363079296)

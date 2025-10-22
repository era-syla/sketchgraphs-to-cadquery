import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.03156, 0.0).lineTo(0.03156, 0.01546).lineTo(0.01364, 0.01546).lineTo(0.01364, 0.02663).lineTo(0.0, 0.02663).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.059993347563791606)

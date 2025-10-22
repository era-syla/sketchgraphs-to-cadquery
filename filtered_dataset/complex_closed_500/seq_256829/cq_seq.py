import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, -0.0).lineTo(0.0127, -0.0).lineTo(0.0127, -0.0127).lineTo(0.0, -0.0127).lineTo(0.0, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.027107470534880898)

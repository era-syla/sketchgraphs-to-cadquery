import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0127).lineTo(-0.07239, 0.0127).lineTo(0.0, 0.04368).lineTo(-0.0, 0.0127).close()
solid=wp_sketch0.add(loop0).extrude(-0.15721694603342914)

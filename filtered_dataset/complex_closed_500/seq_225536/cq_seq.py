import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 8.46).lineTo(4.02, 8.46).lineTo(4.02, 4.54).lineTo(4.17, 4.54).lineTo(4.17, 8.96).lineTo(0.0, 8.96).lineTo(0.0, 8.46).close()
solid=wp_sketch0.add(loop0).extrude(-4.0194929376693445)

import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00229, 0.0026).threePointArc((0.00162, 0.00422), (0.0, 0.00489)).lineTo(0.0, 0.0026).lineTo(0.00229, 0.0026).close()
solid=wp_sketch0.add(loop0).extrude(0.0005932422630206964)

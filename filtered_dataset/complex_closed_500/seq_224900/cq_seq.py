import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.10307, 0.0294).lineTo(0.10013, 0.0294).lineTo(0.10013, -0.0214).lineTo(-0.10307, -0.0214).lineTo(-0.10307, 0.0294).close()
solid=wp_sketch0.add(loop0).extrude(-0.31176207934390493)

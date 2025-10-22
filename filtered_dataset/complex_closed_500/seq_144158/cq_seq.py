import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0381, 0.889).lineTo(-0.2921, 0.44906).lineTo(-0.0381, 0.44906).lineTo(-0.0381, 0.889).close()
solid=wp_sketch0.add(loop0).extrude(-0.16156412052091404)

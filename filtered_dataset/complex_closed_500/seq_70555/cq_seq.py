import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04, -0.103).lineTo(-0.04823, -0.103).lineTo(-0.04823, -0.10125).lineTo(-0.04, -0.103).close()
solid=wp_sketch0.add(loop0).extrude(-0.014993418761563553)
